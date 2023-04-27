const deleteButton = document.querySelector('#delete-button');
const deleteForm = document.querySelector('#delete-form');

deleteButton.addEventListener('click', () => {
    const confirmDelete = confirm('Do you really want to delete this idea? It cancome handy in the future!');
    if (confirmDelete) {
        deleteForm.submit();
    }
})

const form = document.querySelector('#add-idea-form');
form.addEventListener('submit', (event) => {
    event.preventDefault();
    const description = event.target.elements.description.value;
    const message = `You added the idea: "${description}"`;
    alert(message);
    form.submit();
    event.target.elements.description.focus();
});


const editForm = document.querySelector('#edit-form');
editForm.addEventListener('submit', (event) => {
    const description = event.target.elements.description.value.trim();
    if (description === '') {
        event.preventDefault();
        const errorMessage = document.createElement('p');
        errorMessage.textContent = 'You cannot edit this item without adding something.';
        errorMessage.style.color = 'red';
        const formGroup = editForm.parentElement;
        formGroup.appendChild(errorMessage);
    }
});

const textareas = document.querySelectorAll('textarea');
textareas.forEach((textarea) => {
    textarea.addEventListener('keydown', (event) => {
        if (event.keyCode === 13 && !event.shiftKey) {
            event.preventDefault();
            form.submit();
        }
    });
});