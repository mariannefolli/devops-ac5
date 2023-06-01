function insert() {
    let data = {element: "barium"};
    fetch("http://localhost:8080/insert", {
        method: "POST",
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(data)
    }).then(res => {
        console.log(res);
        alert("Usuário criado com sucesso");
    }).catch((_) => {
        alert("Erro ao criar usuário")
    });
}