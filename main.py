from flask import Flask, render_template,request,redirect,url_for
from models import Crear, Equipos, Infraestructura, Personal, Inventario, Ugestion, Costos, Tareas
import db

app = Flask(__name__)

#---------PAGINAS PRINCIPALES------------------------------------------------
@app.route("/")
def home():
    datos= db.session.query(Ugestion).group_by(Ugestion.nombre).all()
    return render_template("index.html", datos= datos)

@app.route("/recursos")
def recursos():
    return render_template("recursos.html")

@app.route("/unidades_gestion/<var>")
def unidad_gestion(var):
    valores= db.session.query(Ugestion.nombre, Ugestion.parcela, Ugestion.fecha).where(Ugestion.nombre==var).all()
    return render_template("unidades_gestion.html", valores=valores)

@app.route("/tareas")
def tareas():
    parcelas = db.session.query(Crear).all()
    equipos = db.session.query(Equipos).all()
    personal = db.session.query(Personal).all()
    inventario = db.session.query(Inventario).all()
    datos = db.session.query(Ugestion).all()
    tareas= db.session.query(Tareas).all()

    return render_template("tareas.html", tareas= tareas, datos=datos, parcelas=parcelas, equipos=equipos, personal=personal,
                           inventario=inventario)

@app.route("/parcelas")
def parcelas():
    datos= db.session.query(Crear).all()
    return render_template("parcelas.html", datos=datos)

@app.route("/inventario")
def inventario():
    datos = db.session.query(Inventario).all()
    return render_template("inventario.html", datos=datos)


@app.route("/equipos")
def equipos():
    datos= db.session.query(Equipos).all()
    return render_template("equipos.html", datos=datos)

@app.route("/personal")
def personal():
    datos= db.session.query(Personal).all()
    return render_template("personal.html", datos=datos)

@app.route("/infraestructura")
def infraestructura():
    datos= db.session.query(Infraestructura).all()
    return render_template("infraestructura.html", datos=datos)
#---------FORMULARIOS-----------------------------------------------------------------


@app.route("/parcela-explo")
def parcela_explo():
    datos= db.session.query(Crear).all()
    return render_template("parcela-explo.html", datos=datos)
#---------------------INFORMACIÓN----------------------------------------------

@app.route("/info_parcela/<id>")
def parcela_info(id):
    datos = db.session.query(Crear).filter_by(id=id)
    return render_template("info_parcela.html", datos=datos)

#-------------------------CREAR------------------------------------------------------

@app.route("/crear_parcela", methods=['POST'])
def asignarparcela():
    valores= Crear(nombre=request.form["nombre"],comunidad=request.form["comunidad"],provincia=request.form["provincia"],municipio=request.form["municipio"],poligono=request.form["poligono"],parcela=request.form["parcela"],recinto=request.form["recinto"],especie=request.form["especie"],variedad=request.form["variedad"],edad=request.form["edad"],estado=request.form["estado"],superficie=request.form["superficie"],plantas=request.form["plantas"],secano=request.form["secano"],aire_libre=request.form["aire_libre"])
    db.session.add(valores)
    db.session.commit()
    db.session.close()
    return redirect(url_for('parcelas'))

@app.route("/crear_tarea", methods=['POST'])
def crear_tarea():
    valores= Tareas(parcela_tratar=request.form["parcela_tratar"],unidades_tratar=request.form["unidades_tratar"],tipo_labor=request.form["tipo_labor"],labores=request.form["labores"],tratar=request.form["tratar"],fertilizar=request.form["fertilizar"],prioridad=request.form["prioridad"],equipos=request.form["equipos"],personal=request.form["personal"],productos=request.form["productos"], fecha=request.form["fecha"])
    db.session.add(valores)
    db.session.commit()
    db.session.close()
    return redirect(url_for('tareas'))

@app.route("/crear_producto", methods=['POST'])
def asignarproducto():
    valores= Inventario(tipo_producto=request.form["tipo_producto"], producto=request.form["producto"],registro=request.form["registro"], abono=request.form["abono"],descripcion=request.form["descripcion"],fabricante=request.form["fabricante"],ingrediente=request.form["ingrediente"],autorizado=request.form["autorizado"],caducidad=request.form["caducidad"])
    db.session.add(valores)
    db.session.commit()
    cantidades= Costos(cantidad= request.form["cantidad"], unidades= request.form["unidades"], unidades_c= request.form["unidades_c"], costo= request.form["costo"], id_inventario=(valores.id))
    db.session.add(cantidades)
    db.session.commit()
    db.session.close()
    return redirect(url_for('inventario'))

@app.route("/crear_equipo", methods=['POST'])
def asignarequipo():
    valores= Equipos(nombre=request.form["nombre"],fecha=request.form["fecha"],matricula=request.form["matricula"],modelo=request.form["modelo"],marca=request.form["marca"],serie=request.form["serie"],tipo=request.form["tipo"],roma=request.form["roma"])
    db.session.add(valores)
    db.session.commit()
    db.session.close()
    return redirect(url_for('equipos'))

@app.route("/crear_personal", methods=['POST'])
def asignarpersonal():
    valores= Personal(nombre=request.form["nombre"],apellido=request.form["apellido"],nif=request.form["nif"],direccion=request.form["direccion"],poblacion=request.form["poblacion"],ciudad=request.form["ciudad"],pais=request.form["pais"],movil=request.form["movil"],correo=request.form["correo"],carnet=request.form["carnet"],rol=request.form["rol"])
    db.session.add(valores)
    db.session.commit()
    db.session.close()
    return redirect(url_for('personal'))

@app.route("/crear_infraestructura", methods=['POST'])
def asignarinfraestructura():
    valores= Infraestructura(nombre=request.form["nombre"],direccion=request.form["direccion"],poblacion=request.form["poblacion"],ciudad=request.form["ciudad"],pais=request.form["pais"],local=request.form["local"])
    db.session.add(valores)
    db.session.commit()
    db.session.close()
    return redirect(url_for('infraestructura'))

@app.route("/crear_explo", methods=['POST'])
def asignarexplo():
    options= request.form.getlist("parcela")
    for op in options:
        valores= Ugestion(nombre=request.form["nombre"], fecha= request.form["fecha"], parcela=op)
        db.session.add(valores)
    db.session.commit()
    db.session.close()
    return redirect(url_for('home'))

#----------------------EDITAR-----------------------------------------------

@app.route('/editar/<tipo>/<id>', methods=['POST'])
def editar(tipo,id):
    if tipo == '1':
        parcela = db.session.query(Crear).filter_by(id=id).first()
        if parcela:
            parcela.especie = request.form['especie']
            parcela.variedad = request.form['variedad']
            parcela.edad = request.form['edad']
            parcela.estado = request.form['estado']
            parcela.plantas = request.form['plantas']
            parcela.secano = request.form['secano']
            parcela.aire_libre = request.form['aire_libre']
            db.session.commit()
            db.session.close()
        return redirect(url_for('parcelas'))
    elif tipo == '2':
        print(id)
        parcela = db.session.query(Costos).filter_by(id_inventario=id).first()
        if parcela:
            parcela.cantidad = request.form['cantidad']
            parcela.unidades_c = request.form['unidades_c']
            db.session.commit()
            db.session.close()
        return redirect(url_for('inventario'))

#---------------ELIMINAR----------------------------------
@app.route('/eliminar/<tipo>/<id>')
def eliminar(tipo, id):
    if tipo == '1':
        tesoreria = db.session.query(Crear).filter_by(id=id).first()
        db.session.delete(tesoreria)
        db.session.commit()
        db.session.close()
        return redirect(url_for('parcelas'))
    elif tipo == '2':
        tesoreria = db.session.query(Equipos).filter_by(id=id).first()
        db.session.delete(tesoreria)
        db.session.commit()
        db.session.close()
        return redirect(url_for('equipos'))
    elif tipo == '3':
        tesoreria = db.session.query(Personal).filter_by(id=id).first()
        db.session.delete(tesoreria)
        db.session.commit()
        db.session.close()
        return redirect(url_for('personal'))
    elif tipo == '4':
        tesoreria = db.session.query(Infraestructura).filter_by(id=id).first()
        db.session.delete(tesoreria)
        db.session.commit()
        db.session.close()
        return redirect(url_for('infraestructura'))
    elif tipo == '5':
        tesoreria = db.session.query(Inventario).filter_by(id=id).first()
        costes = db.session.query(Costos).filter_by(id_inventario=id).first()
        db.session.delete(tesoreria)
        db.session.delete(costes)
        db.session.commit()
        db.session.close()
        return redirect(url_for('inventario'))

if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    app.secret_key = 'super secret key'
    app.jinja_env.globals.update(zip=zip)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
