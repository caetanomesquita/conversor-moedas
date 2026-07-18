const form = document.getElementById("form-conversor");

async function converter() {
  const valor = document.getElementById("valor").value;
  const de = document.getElementById("de").value;
  const para = document.getElementById("para").value;
  const resultado = document.getElementById("resultado");

  const url = `/api/convert?de=${de}&para=${para}&valor=${valor}`;

  const resposta = await fetch(url);
  const dados = await resposta.json();

  if (dados.erro) {
    resultado.textContent = dados.erro;
  } else {
    resultado.textContent = `${valor} ${de} = ${dados.resultado} ${para}`;
  }
}

const botaoInverter = document.getElementById("botao-inverter");

botaoInverter.addEventListener("click", function () {
  const selectDe = document.getElementById("de");
  const selectPara = document.getElementById("para");

  const valorTemporario = selectDe.value;
  selectDe.value = selectPara.value;
  selectPara.value = valorTemporario;
});

form.addEventListener("keydown", function (evento) {
  if (evento.key === "Enter") {
    evento.preventDefault();
    converter();
  }
});

form.addEventListener("submit", function (evento) {
  evento.preventDefault();
  converter();
});