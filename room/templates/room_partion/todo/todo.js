<script>
  function toggletodostatus(todo_id){
    
      console.log(todo_id)
      fetch(`/togglestatus/${todo_id}` , {
          method: 'GET',
          headers: {
              'Content-Type': 'application/json'
          }
      })
      .then(response => response.json())
      .then(data => {
          console.log(data)

          if (data['todo']['is_done'] == true){
              document.getElementById(todo_id).style.textDecoration = "line-through";
          }
          else{
              document.getElementById(todo_id).style.textDecoration = "none";
          }

      })
  }

</script>