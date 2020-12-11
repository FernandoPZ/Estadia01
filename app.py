'''  
NOMBRE: Maria del Carmen Hernandez Diaz
ACCOUNT: 1718110389
GROUP: TIC 51
DATE: 09-08-2020
DESCRIPTION: Update and delete objetive
'''

import web

urls = [
    '/horario/?','mvc.controllers.alumnos.horario.Horario',
    '/view/(.*)','mvc.controllers.alumnos.view.View',
    '/carga/?','mvc.controllers.alumnos.cargaacademica.CargaAcademica',
    '/profile/?','mvc.controllers.alumnos.profile.Profile',
    '/login','mvc.controllers.alumnos.login.Login',

] # COLOCAMOS LA RUTA

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
