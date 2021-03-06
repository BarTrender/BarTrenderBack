from rest_framework.response import Response

errors = {
    'A001': 'Client no existe',
    'A002': 'Owner no existe',
    'A003': 'No se encuentra la API KEY',
    'A004': 'API KEY Incorrecta',
    'A005': 'No se encuentra el Token',
    'A006': 'Token invalido',
    'A007': 'El token ha expirado',
    'A008': 'No tienes permiso para realizar esta acción',
    'A009': 'Email o Contraseña incorrectos',
    'A010': 'No se ha podido obtener el rol del token',
    'A011': 'El rol proporcionado no es correcto',
    'A012': 'No se ha podido crear el usuario',
    'A013': 'Un usuario con este correo ya existe',
    'A014': 'Un usuario con este teléfono ya existe',
    'A015': 'Email no valido',
    'A016': 'La contraseña debe contener 8 dígitos, y al menos una mayúscula, una minúscula, un número y un caracter especial',
    'A017': 'El usuario que está logeado no es premium',
    'A018': 'Contraseña incorrecta',
    'A019': 'Error al intentar hacer login con las API de Google',
    'E001': 'Establecimiento no existe',
    'E002': 'El establecimiento no pertenece al dueño',
    'E003': 'Las etiquetas indicadas no existen',
    'E004': 'Error al borrar el establecimiento. Tienes un/varios pago/s pendiente/s',
    'D001': 'Descuento no existe',
    'D002': 'Descuento no pertenece al establecimiento',
    'D003': 'El descuento ha expirado',
    'D004': 'No quedan descuentos disponibles',
    'D005': 'Descuento ya escaneado por usuario',
    'D010': 'Campos obligatorios no proporcionados',
    'D011': 'El coste no puede ser menor que 0',
    'D012': 'El total de códigos no puede ser menor que 0',
    'D013': 'La fecha inicial no puede estar en el pasado',
    'D014': 'La fecha de finalización debe ser posterior a la inicial',
    'D015': 'El total de códigos no puede ser menor que 0 ni que el número de códigos escaneados',
    'D016': 'La fecha de finalización debe ser posterior a la inicial y posterior a la actual',
    'D017': 'Los parámetros nombre, descripción, coste, fecha de inicio y códigos escaneados no pueden ser modificados una vez empezado el descuento',
    'D018': 'El número de códigos escaneados no puede ser diferente de 0',
    'D019': 'No se puede modificar un descuento que haya caducado',
    'D020': 'No se puede eliminar un descuento que haya comenzado y tenga códigos escaneados',
    'D021': 'El descuento aun no ha comenzado',
    'D022': 'Query invalida',
    'D023': 'Host inválido',
    'P001': 'El pago aun no ha sido efectuado en paypal. Verifiquelo.',
    'P002': 'Las fechas del pago no coinciden. Sospechoso...',
    'Z001': 'Faltan campos obligatorios en el cuerpo de la petición',
    'Z002': 'Timestamp no valido',
    'Z003': 'Teléfono no válido',
    'Z004': 'Necesitas ser mayor de edad para registrarte en esta aplicación',
    'E00X': 'Ha ocurrido un error inesperado. Contacte con el administrador',
    'API001': 'Error al obtener el token de auth de paypal',
    'API002': 'Error con las orders de paypal. ¿Has puesto bien el ID?',
    'API003': 'Error con la API interna. Pruebe mas tarde',
}


def generate_response(code, status):
    body = {
        'error': str(code) + ": " + errors[code]
    }

    return Response(body, status)
