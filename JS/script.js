let titulo = "Aprender JavaScript";
let descricao = "Estudar manipulação de strings";

console.log("Título: ", titulo);
console.log("Descrição: ", descricao);

console.log("Comprimento do título:", titulo.length);

console.log("Primeiro caracter:", titulo[0]);
console.log("Primeiro caracter:", titulo[titulo.length-1]);
console.log("Caractere na posição 1:", titulo.charAt(1));

let categoria = "Estudo";
let infoCompleta = "Categoria:" + categoria + " - " + titulo;
let infoCompletaTS = `Categoria: ${categoria} - ${titulo}`;

console.log("Concatenação tradicional:", infoCompleta);
console.log("Concatenação template string:", infoCompletaTS);

console.log("Posição inicial de 'JavaScript':", titulo.indexOf("JavaScript"));
console.log("Inclui 'JavaScript':", titulo.includes("JavaScript"));
console.log("Começa com 'JavaScript':", titulo.startsWith("JavaScript"));
console.log("Termina com 'JavaScript':", titulo.endsWith("JavaScript"));

function truncarDescricao(texto, maxLenght = 30) {
    if (texto.length <= maxLenght){
        return texto;
    }
    return texto.substring(0, maxLenght) + "...";
}

console.log(truncarDescricao("Lorem ipsum dolor sit amet consectetur adipisicing elit. Sequi perspiciatis corrupti aperiam, doloribus eligendi minima delectus itaque sit ex vitae quos amet. Facere, illo temporibus nam excepturi esse natus minima?"));
console.log("TEXTO TEXTO".slice(0, 3));

let tags = "javascript,programação,web,frontend";
let arrayTags = tags.split(",");

console.log(tags);
console.log(arrayTags);

let stringTags = arrayTags.join("-");
console.log(stringTags);

let nome = "araraquara";
console.log(nome.replace("a","B"));

console.log("Math.PI:", Math.PI);
console.log("Math.E:", Math.E);

const raio = 5;
const areaCirculo = Math.PI * Math.pow(raio, 2);
console.log(`Área de um círculo com raio ${raio}: ${areaCirculo}`);

const numero = 9.7;
console.log(numero.toFixed(4));

function numeroAleatorioEntre(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

console.log("Número aleatório entre 1 e 10:", numeroAleatorioEntre(1, 10))

const hoje = new Date();
console.log("Data atual: ", hoje.toString());