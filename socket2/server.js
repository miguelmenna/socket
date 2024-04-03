const net = require('net');
const fs = require('fs');
const path = require('path');

const server = net.createServer(socket => {
    console.log('Cliente conectado.');

    socket.on('data', data => {
        const url = data.toString();
        const filePath = path.join(__dirname, url);

        fs.readFile(filePath, (err, fileData) => {
            if (err) {
                console.error(err);
                socket.write('Arquivo não encontrado.');
                return;
            }
            socket.write(fileData);
            console.log(`Arquivo ${url} enviado para o cliente.`);
        });
    });

    socket.on('end', () => {
        console.log('Cliente desconectado.');
    });
});

const PORT = process.argv[2] || 8088; // Porta fornecida como argumento ou padrão 8088
const DIRECTORY = process.argv[3] || __dirname; // Diretório fornecido como argumento ou diretório atual
server.listen(PORT, () => {
    console.log(`Servidor escutando na porta ${PORT}`);
    console.log(`Diretório raiz: ${DIRECTORY}`);
});
