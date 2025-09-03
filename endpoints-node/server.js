import express from "express";

const app =
  express(); /*cunado escribis una variable en mayuscula va a seer constante realmente nunca va a 
cambiar*/
const PORT = 3000;

app.use(express.json());

app.get("/", (req, res) => {
  res.send("Este e s un endpoint hecho con expres");
});

//endpoint con parametro

app.get("/api/user/:id", (req, res) => {
  //destructuracion
  const { id } = req.params; //captura el valor de un objeto atravez de las llaves {}
  res.send({ message: `El usuario con id ${id} es Pepito` });
});

app.get("/api/search", (req, res) => {
  const { name, lastname } = req.query; //el query empieza cuando s eabre el signo de pregunta y usamos la variable de las llaves para pasrle un valor
  res.json({
    firstName: name,
    lastname,
  });
});

app.post("/api/user", (req, res) => {
  const { name, email } = req.body;
  res.json({ mensaje: "Usuario creado", data: { name, email } });
});

app.listen(PORT, () => {
  console.log(`Servidor corriendo en el puerto ${PORT}`);
}); /*SIRVE PARA QUE CORRA EL PUERTO CONSTANTEMENTE*/
