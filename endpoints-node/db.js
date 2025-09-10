import mysql from "mysql2/promise"
import dotenv from "dotenv"

dotenv.config();//carga las variables

//configuracion de la conexion
const pool = mysql.createPool(
    {
        host: process.env.DB_HOST,
        user: process.env.DB_USER,
        password: process.env.DB_PASSWORD,
        database: process.env.DB_DATABASE,
        waitForConnections: true,//espera es que este dsipnible el servidor 
        connectionLimit: 10,// cuans personas s epueden conectar
        queueLimit: 0//la cantidad de cpnexiones que pueden quedar en espera 
    }
);

export default pool;