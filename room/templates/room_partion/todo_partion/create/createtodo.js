<script>
    let submitbutton  = document.getElementById('submit-todo-form')
    submitbutton.onclick = addtodo
    function addtodo() {
        let form  = document.getElementById('add-todo-form')
        let title  = document.getElementById('title').value
        let csrftoken = document.querySelector('[name = csrfmiddlewaretoken]')
        let formData = new FormData();
        formData.append('title' , title);
        formData.append('id' , {{room.id}});
        fetch('/addtodo/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': csrftoken.value
            },
        })
        .then(response => response.json())
        .then(data => {
            
            console.log("okkkk");
            console.log(data);
            
            if (data['todo']){
                let todos_ul = document.getElementById('todos')
            let activetodos = document.getElementById('activetodos')
            let createdtodo = `
            <li
            class="list-group-item d-flex align-items-center border-0 mb-2 rounded"
            style="background-color: #f4f6f7"
            >
            <input
                class="form-check-input me-2"
                type="checkbox"
                value=""
                aria-label="..."
            />
            <span>${data['todo']['title']}</span>
            </li>
            `
            let tempDiv = document.createElement('div');
            tempDiv.innerHTML = createdtodo;
            todos_ul.appendChild(tempDiv);

            let tempDiv2 = document.createElement('div');
            tempDiv2.innerHTML = createdtodo;
            activetodos.appendChild(tempDiv2);
            form.reset();
            }
        })        
    }
</script>
