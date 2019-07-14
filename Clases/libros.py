# -- Creación de la clase objeto Libro.
lugares = {'ASIA': .7, 'AMERICA': .10, 'EUROPA': .14}


class libro(object):

    def __init__(self, isbn, titulo, categoria, fecha_publicacion,
                 lugar_publicacion, estado, idioma, autor, editorial,
                 cantidad_pag, precio):
        global lugares
        self.isbn = isbn
        self.titulo = titulo
        self.categoria = categoria
        self.fecha_publicacion = fecha_publicacion
        self.lugar_publicacion = lugar_publicacion
        self.autor = autor
        self.estado = estado
        self.idioma = idioma
        self.editorial = editorial
        self.cantidad_pag = cantidad_pag
        self.precio_base = precio
        lugar = lugar_publicacion.upper()
        self.precio_neto = (float(precio) * lugares.get(lugar))+float(precio)
        descuento = 0
        estado_libro = estado.upper()
        if estado_libro == 'USADO':
            descuento = float(self.precio_neto)*.15
            pass
        self.precio_final = ((float(self.precio_neto) -
                              descuento)+float(self.precio_neto)*.19)
        pass

    def datos_completos(self):
        return print('Datos del libro:\n\n',
                     'ISBN: ', self.isbn,
                     '\nTitulo: ', self.titulo,
                     '\nCategoría: ', self.categoria,
                     '\nFecha de publicación: ', self.fecha_publicacion,
                     '\nLugar de publicación: ', self.lugar_publicacion,
                     '\nAutor: ', self.autor,
                     '\nEstado: ', self.estado,
                     '\nIdioma: ', self.idioma,
                     '\nEditorial: ', self.editorial,
                     '\nCantidad de paginas: ', self.cantidad_pag,
                     '\nPrecio Neto: ', self.precio_neto,
                     '\nPrecio Final: ', self.precio_final)
