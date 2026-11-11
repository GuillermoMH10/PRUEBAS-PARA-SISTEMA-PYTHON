document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('contactForm');
    const panelForm = document.querySelector('.panel-form');
    const formTitle = document.getElementById('formTitle');
    const btnSubmit = document.getElementById('btnSubmit');
    const btnCancelEdit = document.getElementById('btnCancelEdit');
    const contactoIdInput = document.getElementById('contactoId');

    const inputNombre = document.getElementById('nombre');
    const inputApellido = document.getElementById('apellido');
    const inputTelefono = document.getElementById('telefono');
    const inputCorreo = document.getElementById('correo');

    const tableBody = document.getElementById('tableBody');
    const emptyState = document.getElementById('emptyState');
    const totalCount = document.getElementById('totalCount');
    const searchInput = document.getElementById('searchInput');
    const toast = document.getElementById('toast');

    let toastTimer = null;

    function showToast(msg) {
        toast.textContent = msg;
        toast.classList.remove('hidden');
        clearTimeout(toastTimer);
        toastTimer = setTimeout(() => {
            toast.classList.add('hidden');
        }, 2200);
    }

    function updateCounterAndEmptyState() {
        const rows = tableBody.querySelectorAll('tr');
        totalCount.textContent = rows.length;
        if (rows.length === 0) {
            emptyState.classList.remove('hidden');
        } else {
            emptyState.classList.add('hidden');
        }
    }

    function escapeHtml(str) {
        const div = document.createElement('div');
        div.textContent = str || '';
        return div.innerHTML;
    }

    function buildRow(c) {
        const tr = document.createElement('tr');
        tr.dataset.id = c.id;
        tr.dataset.nombre = c.nombre;
        tr.dataset.apellido = c.apellido;
        tr.dataset.telefono = c.telefono;
        tr.dataset.correo = c.correo;

        tr.innerHTML = `
            <td class="cell-primary">${escapeHtml(c.nombre)}</td>
            <td>${escapeHtml(c.apellido)}</td>
            <td class="cell-mono">${escapeHtml(c.telefono)}</td>
            <td class="cell-muted">${escapeHtml(c.correo)}</td>
            <td class="col-actions">
                <div class="row-actions">
                    <button type="button" class="action-btn btn-edit" title="Editar">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M12 20h9"></path>
                            <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
                        </svg>
                    </button>
                    <button type="button" class="action-btn btn-delete" title="Eliminar">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <polyline points="3 6 5 6 21 6"></polyline>
                            <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                        </svg>
                    </button>
                </div>
            </td>
        `;
        return tr;
    }

    function resetForm() {
        form.reset();
        contactoIdInput.value = '';
        formTitle.textContent = 'Nuevo registro';
        btnSubmit.textContent = 'Guardar';
        btnCancelEdit.classList.add('hidden');
        panelForm.classList.remove('editing');
        tableBody.querySelectorAll('tr.active-row').forEach(r => r.classList.remove('active-row'));
    }

    btnCancelEdit.addEventListener('click', resetForm);

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const id = contactoIdInput.value.trim();
        const payload = {
            nombre: inputNombre.value.trim(),
            apellido: inputApellido.value.trim(),
            telefono: inputTelefono.value.trim(),
            correo: inputCorreo.value.trim()
        };

        const isEdit = Boolean(id);
        const url = isEdit ? `/api/contactos/${id}` : '/api/contactos';
        const method = isEdit ? 'PUT' : 'POST';

        btnSubmit.disabled = true;

        try {
            const res = await fetch(url, {
                method,
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const result = await res.json();

            if (!res.ok || !result.ok) {
                showToast(result.error || 'Error al guardar');
                return;
            }

            const contacto = result.data;
            if (isEdit) {
                const existingRow = tableBody.querySelector(`tr[data-id="${id}"]`);
                if (existingRow) {
                    existingRow.replaceWith(buildRow(contacto));
                }
                showToast('Registro actualizado');
            } else {
                tableBody.prepend(buildRow(contacto));
                showToast('Registro guardado');
            }

            resetForm();
            updateCounterAndEmptyState();
        } catch (err) {
            showToast('Error de conexión');
        } finally {
            btnSubmit.disabled = false;
        }
    });

    tableBody.addEventListener('click', async (e) => {
        const editBtn = e.target.closest('.btn-edit');
        const deleteBtn = e.target.closest('.btn-delete');
        const row = e.target.closest('tr');
        if (!row) return;

        const id = row.dataset.id;

        if (editBtn) {
            tableBody.querySelectorAll('tr.active-row').forEach(r => r.classList.remove('active-row'));
            row.classList.add('active-row');

            contactoIdInput.value = id;
            inputNombre.value = row.dataset.nombre;
            inputApellido.value = row.dataset.apellido;
            inputTelefono.value = row.dataset.telefono;
            inputCorreo.value = row.dataset.correo;

            formTitle.textContent = 'Editar registro';
            btnSubmit.textContent = 'Actualizar';
            btnCancelEdit.classList.remove('hidden');
            panelForm.classList.add('editing');
            inputNombre.focus();
        }

        if (deleteBtn) {
            try {
                const res = await fetch(`/api/contactos/${id}`, { method: 'DELETE' });
                const result = await res.json();
                if (res.ok && result.ok) {
                    if (contactoIdInput.value === id) {
                        resetForm();
                    }
                    row.remove();
                    updateCounterAndEmptyState();
                    showToast('Registro eliminado');
                }
            } catch (err) {
                showToast('Error al eliminar');
            }
        }
    });

    searchInput.addEventListener('input', () => {
        const q = searchInput.value.toLowerCase().trim();
        const rows = tableBody.querySelectorAll('tr');
        rows.forEach(row => {
            const text = [
                row.dataset.nombre,
                row.dataset.apellido,
                row.dataset.telefono,
                row.dataset.correo
            ].join(' ').toLowerCase();
            row.style.display = text.includes(q) ? '' : 'none';
        });
    });
});
