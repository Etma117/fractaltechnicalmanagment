from reportlab.pdfgen import canvas
from django.http import HttpResponse

def generate_ticket(purchase):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="ticket_{purchase.id}.pdf"'

    # Crear el objeto PDF
    p = canvas.Canvas(response)

    # Agregar contenido al PDF
    p.drawString(100, 800, f'Ticket de Compra #{purchase.id}')
    p.drawString(100, 780, f'Fecha: {purchase.fecha}')
    p.drawString(100, 760, f'Cliente: {purchase.cliente.nombre}')
    # Agrega más detalles según tus necesidades

    # Cierra el objeto PDF
    p.showPage()
    p.save()

    return response