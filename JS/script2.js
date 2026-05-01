const tarefas = ["Preparar", "Estudar", "Teste"];

console.log(tarefas);
console.log(tarefas[0]);
console.log(tarefas[tarefas.length - 1]);

tarefas[0] = "Prepare"; //modificação indireta, pois é const
console.log(tarefas[0]);

tarefas.push("Validar");
console.log(tarefas);

tarefas.pop();
console.log(tarefas);

tarefas.unshift("Validar");
console.log(tarefas);

tarefas.shift();
console.log(tarefas);

tarefas.splice(1, 1); //Apagar
console.log(tarefas);

tarefas.splice(1,0,"Estudar"); //Adicionar
console.log(tarefas);

tarefas.splice(2,1,"Validar"); //Substituir
console.log(tarefas);

tarefas.forEach((elemento, indice) => {
    console.log(indice+1);
});

const tarefas_novo = tarefas.map((T, i) => T.toUpperCase())
console.log(tarefas_novo)

const tarefas_novo_filter = tarefas.filter((T, i) => T.includes("t"))
console.log(tarefas_novo_filter)

const tarefas_novo_find = tarefas.find((T, i) => T.includes("a"))
console.log(tarefas_novo_find)

const tarefas_novo_find_index = tarefas.findIndex((T, i) => T.includes("a"))
console.log(tarefas_novo_find_index)

const tarefas_novo_reduce = tarefas.reduce((Acumulador, elemento, index) => Acumulador + elemento[index].length)
console.log(tarefas_novo_reduce)

const [elemento, elemento1, elemento2] = tarefas
const tarefas2 = [...tarefas] //assim não há interligação

//tipo de retorno  sem 'return' numa function === retorno implícito