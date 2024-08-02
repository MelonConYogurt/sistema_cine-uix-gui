document.getElementById('asientos_form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const sala = document.getElementById('id_nombres_salas_input').value;
    const numeroAsiento = document.getElementById('id_numero_asientos_input').value;
    const seccionAsiento = document.getElementById('id_seccion_asientos_input').value;
    let fechaAsiento = document.getElementById('id_fecha_asientos_input').value;

    // Añadir segundos si no están presentes
    if (fechaAsiento.length === 16) {
        fechaAsiento += ':00';
    }

    // Convertir a formato requerido por MySQL (YYYY-MM-DD HH:MM:SS)
    const formattedFechaAsiento = fechaAsiento.replace('T', ' ');

    const data = {
        sala: sala,
        numero_asiento: numeroAsiento,
        seccion_asiento: seccionAsiento,
        fecha_asiento: formattedFechaAsiento
    };

    try {
        const response = await fetch('http://127.0.0.1:8000/crear/asientos/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        console.log('Success:', result);
        alert('Asiento añadido con éxito');
    } catch (error) {
        console.error('Error:', error);
        alert('Error al añadir el asiento');
    }
});

document.getElementById('peliculas_form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const titulo = document.getElementById('id_titulo_peliculas_input').value;
    const genero = document.getElementById('id_genero_pelicula_input').value;
    const duracion = document.getElementById('id_duracion_pelicula_input').value;
    const rating = document.getElementById('id_rating_pelicula_input').value;

    const data = {
        titulo_pelicula: titulo,
        genero_pelicula: genero,
        duracion_pelicula: duracion,
        rating_pelicula: rating
    };

    try {
        const response = await fetch('http://127.0.0.1:8000/crear/peliculas/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        console.log('Success:', result);
        alert('Película añadida con éxito');
    } catch (error) {
        console.error('Error:', error);
        alert('Error al añadir la película');
    }
});


document.getElementById('salas_form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const nombre = document.getElementById('id_nombre_sala_input').value;
    const capacidad = document.getElementById('id_capacidad_sala_input').value;
    const estado = document.getElementById('id_estado_sala_input').value;

    const data = {
        nombre_sala: nombre,
        capacidad_sala: capacidad,
        estado_sala: estado,
    };

    try {
        const response = await fetch('http://127.0.0.1:8000/crear/salas/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        console.log('Success:', result);
        alert('Película añadida con éxito');
    } catch (error) {
        console.error('Error:', error);
        alert('Error al añadir la película');
    }
});

