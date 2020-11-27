from django.db import models
from django.contrib.auth.models import User

class Adminsitrador(models.Model):
    id_administrador = models.CharField(primary_key=True,max_length=10)
    primer_nombre = models.CharField(max_length=20,null=True)
    apellido_paterno = models.CharField(max_length=20,null=True)
    permisos = models.CharField(max_length=20,null=True)
    ad_id_usuario = models.CharField(max_length=20,null=True) 

    class Meta:
        managed = False
        db_table = 'adminsitrador'

class Alergia(models.Model):
    id_alergia = models.CharField(primary_key=True,max_length=10)  
    nombre = models.CharField(max_length=50,null=True)
    descripcion = models.CharField(max_length=100,null=True)

    class Meta:
        managed = False
        db_table = 'alergia'

class BotAyuda(models.Model):
    idbot = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'bot_ayuda'

class CentroAtencion(models.Model):
    id_centro = models.CharField(primary_key=True,max_length=10)  
    nombre_centro = models.CharField(max_length=20,null=True)
    ubicacion = models.CharField(max_length=50,null=True)

    class Meta:
        managed = False
        db_table = 'centro_atencion'

class Cirugia(models.Model):
    id_cirugia = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    nombre = models.CharField(max_length=40,null=True)
    descripcion = models.CharField(max_length=100,null=True)
    area_afectada = models.CharField(max_length=100,null=True)

    class Meta:
        managed = False
        db_table = 'cirugia'

class Ciudad(models.Model):
    id_ciudad = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    nombre = models.CharField(max_length=50,null=True)

    class Meta:
        managed = False
        db_table = 'ciudad'

class Comuna(models.Model):
    id_comuna = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    nombre_comuna = models.CharField(max_length=50)
    cmid_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='cmid_ciudad')

    class Meta:
        managed = False
        db_table = 'comuna'

class Cupo(models.Model):
    id_cupo = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    detalle_cupo = models.CharField(max_length=100,null=True)

    class Meta:
        managed = False
        db_table = 'cupo'

class CupoTaller(models.Model):
    cp_id_cupo = models.CharField(max_length=100)  # This field type is a guess.
    t_id_taller = models.CharField(max_length=100)  # This field type is a guess.
    f_id_ficha = models.CharField(max_length=100)  # This field type is a guess.
    capacidad = models.CharField(max_length=100)  # This field type is a guess.
    inscripcion = models.CharField(max_length=100,null=True)

    class Meta:
        managed = False
        db_table = 'cupo_taller'
# Unable to inspect table 'detalle_diagnotico'
# The error was: list index out of range

class DetalleInforme(models.Model):
    df_id_informe = models.CharField(max_length=20,null=True)
    df_id_administrador = models.CharField(max_length=20,null=True)  
    hora_creacion = models.DateField(null=True) 
    solicitud = models.CharField(max_length=40,null=True)
    dia_entrega = models.DateField(null=True)

    class Meta:
        managed = False
        db_table = 'detalle_informe'

class DetalleTaller(models.Model):
    id_medi = models.CharField(primary_key=True,max_length=10)  
    de_id_taller = models.CharField(null=True,max_length=10)  
    fecha = models.DateField(null=True)
    hora_inicio = models.DateField(null=True)
    hora_termino = models.DateField(null=True)
    descripcion = models.CharField(max_length=100,null=True)
    duracion_total = models.DateField(null=True)

    class Meta:
        managed = False
        db_table = 'detalle_taller'

class Diagnostico(models.Model):
    id_diagnostico = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    descripcion = models.CharField(max_length=100,null=True)
    ficha_id_ficha = models.CharField(null=True,max_length=10)  # This field type is a guess.
    medico_id_medico = models.CharField(null=True,max_length=10)  # This field type is a guess.
    hallazgo = models.CharField(max_length=50,null=True)
    estado = models.CharField(max_length=50,null=True)

    class Meta:
        managed = False
        db_table = 'diagnostico'

class Enfermedad(models.Model):
    id_enfermedad = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    nombre = models.CharField(max_length=50,null=True)
    descripcion = models.CharField(max_length=100,null=True)
    gravedad = models.CharField(max_length=40,null=True)
    indicaciones = models.CharField(max_length=100,null=True)

    class Meta:
        managed = False
        db_table = 'enfermedad'

class Especialidad(models.Model):
    id_especialidad = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    descripcion = models.CharField(max_length=10,null=True)
    area_especialidad = models.CharField(max_length=20,null=True)

    class Meta:
        managed = False
        db_table = 'especialidad'

class Ficha(models.Model):
    id_ficha = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    domicilio = models.CharField(max_length=50,null=True)
    telefono = models.CharField(null=True,max_length=10)  # This field type is a guess.
    fecha_nacimiento = models.DateField(null=True)
    ficha_id_sangre = models.CharField(null=True,max_length=10)  # This field type is a guess.
    ficha_id_sexo = models.CharField(null=True,max_length=10)  # This field type is a guess.
    ficha_id_centro = models.CharField(null=True,max_length=10)  # This field type is a guess.
    ficha_id_sistema = models.CharField(null=True,max_length=10)  # This field type is a guess.
    estado = models.CharField(max_length=100,null=True)

    class Meta:
        managed = False
        db_table = 'ficha'

class FormularioConsulta(models.Model):
    id_formulario = models.CharField(primary_key=True,max_length=10,db_column='id_formulario',unique=True)  # This field type is a guess.
    motivo_consulta = models.CharField(max_length=100,null=True)
    fc_id_ficha = models.CharField(null=True,max_length=10)  # This field type is a guess.
    sintoma = models.CharField(max_length=100,null=True)
    hora_solicitud = models.CharField(max_length=100, null=True)
    prioridad = models.CharField(max_length=20,null=True)
    

    class Meta:
        managed = False
        db_table = 'formulario_consulta'

class Gruposangre(models.Model):
    id_sangre = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    tipo_sangre = models.CharField(max_length=40,null=True)

    class Meta:
        managed = False
        db_table = 'gruposangre'

class HistorialAlergias(models.Model):
    ha_id_ficha = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    al_id_alergia = models.CharField(max_length=10)  # This field type is a guess.
    tipo = models.CharField(max_length=50,null=True)
    descripcion = models.CharField(max_length=100,null=True)
    prevencion = models.CharField(max_length=100,null=True)
    riesgos = models.CharField(max_length=100,null=True)

    class Meta:
        managed = False
        db_table = 'historial_alergias'

class HistorialCirugias(models.Model):
    hc_id_ficha = models.CharField(null=True,max_length=10)  # This field type is a guess.
    hc_id_cirugia = models.CharField(null=True,max_length=10)  # This field type is a guess.
    tipo = models.CharField(max_length=40,null=True)
    descripcion = models.CharField(max_length=100,null=True)
    fecha_realizacion = models.DateField(null=True)

    class Meta:
        managed = False
        db_table = 'historial_cirugias'

class HistorialMedicamentos(models.Model):
    hm_id_ficha = models.CharField(null=True,max_length=10)  # This field type is a guess.
    hm_id_medicamento = models.CharField(null=True,max_length=10) # This field type is a guess.
    descipcion = models.CharField(max_length=50,null=True)
    tratamiento = models.CharField(max_length=100,null=True)
    dosis_suministrada = models.CharField(max_length=100,null=True)
    horario = models.DateField(null=True)

    class Meta:
        managed = False
        db_table = 'historial_medicamentos'

class HistorialMedico(models.Model):
    fi_id_ficha = models.CharField(null=True,max_length=10)  # This field type is a guess.
    med_id_medico = models.CharField(null=True,max_length=10)  # This field type is a guess.
    descripcion = models.CharField(max_length=100,null=True)
    dia_atencion = models.DateField(null=True)
    observaciones = models.CharField(max_length=100,null=True)
    derivaciones = models.CharField(max_length=100,null=True)
    procedimiento = models.CharField(max_length=100,null=True)

    class Meta:
        managed = False
        db_table = 'historial_medico'

class Informe(models.Model):
    id_informe = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    nombre = models.CharField(max_length=20,null=True)
    descripcion = models.CharField(max_length=100,null=True)
    area = models.CharField(max_length=20,null=True)

    class Meta:
        managed = False
        db_table = 'informe'

class Medicamento(models.Model):
    id_medicamento = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    nombre = models.CharField(max_length=50)
    gramos = models.CharField(max_length=10)  # This field type is a guess.
    descripcion = models.CharField(max_length=100)
    dosis_recomendada = models.CharField(max_length=50)
    laboratorio = models.CharField(max_length=50)
    contraindicacion = models.CharField(max_length=100)
    med_id_tipo_medi = models.CharField(max_length=10)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'medicamento'

class Medico(models.Model):
    id_medico = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    rut = models.CharField(max_length=10)  # This field type is a guess.
    dv = models.CharField(max_length=1)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    md_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='md_id_usuario')
    horario = models.DateField()
    centro_estudio = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'medico'

class Opcion(models.Model):
    id_opcion = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    detalle = models.CharField(max_length=1)
    op_id_pregunta = models.ForeignKey('Pregunta', models.DO_NOTHING, db_column='op_id_pregunta')
    op_id_respuesta = models.ForeignKey('Respuesta', models.DO_NOTHING, db_column='op_id_respuesta')
    op_idbot = models.ForeignKey(BotAyuda, models.DO_NOTHING, db_column='op_idbot')

    class Meta:
        managed = False
        db_table = 'opcion'

class Paciente(models.Model):
    rut = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    dv = models.CharField(max_length=1)
    primer_nombre = models.CharField(max_length=20,null=True)
    segundo_nombre = models.CharField(max_length=20,null=True)
    apellido_paterno = models.CharField(max_length=20,null=True)
    apellido_materno = models.CharField(max_length=20,null=True)
    paci_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='paci_id_usuario')
    edad = models.CharField(null=True,max_length=3)  # This field type is a guess.
    paci_id_ficha = models.ForeignKey(Ficha, models.DO_NOTHING, db_column='paci_id_ficha')

    class Meta:
        managed = False
        db_table = 'paciente'

class Pregunta(models.Model):
    id_pregunta = models.CharField(primary_key=True,max_length=10) 
    descripcion = models.CharField(max_length=100,null=True)

    class Meta:
        managed = False
        db_table = 'pregunta'

class RecordatorioMedico(models.Model):
    id_recordatorio = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    detalle_recordatorio = models.CharField(max_length=100,null=True)
    hora_recordatorio = models.DateField(null=True)
    ficha_id_ficha = models.ForeignKey(Ficha, models.DO_NOTHING, db_column='ficha_id_ficha')

    class Meta:
        managed = False
        db_table = 'recordatorio_medico'

class Respuesta(models.Model):
    id_respuesta = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    descripcion = models.CharField(max_length=100,null=True)

    class Meta:
        managed = False
        db_table = 'respuesta'

class Sexo(models.Model):
    id_sexo = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    nombre = models.CharField(max_length=50,null=True)
    sigla = models.CharField(max_length=2,null=True)
    detalle_genero = models.CharField(max_length=15,null=True)

    class Meta:
        managed = False
        db_table = 'sexo'

class SistemaDeSalud(models.Model):
    id_sistema = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    nombre_sistema = models.CharField(max_length=50,null=True)
    ubicacion = models.CharField(max_length=50,null=True)

    class Meta:
        managed = False
        db_table = 'sistema_de_salud'

class Taller(models.Model):
    id_taller = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    nombre_taller = models.CharField(max_length=100,null=True)
    tema = models.CharField(max_length=100,null=True)

    class Meta:
        managed = False
        db_table = 'taller'

class TipoEspecialidad(models.Model):
    id_esp = models.CharField(null=True,max_length=10)  # This field type is a guess.
    id_med = models.CharField(null=True,max_length=10)  # This field type is a guess.
    nombre = models.CharField(max_length=20,null=True)
    descripcion = models.CharField(max_length=100,null=True)
    orientacion = models.CharField(max_length=20,null=True)

    class Meta:
        managed = False
        db_table = 'tipo_especialidad'

class TipoMedicamento(models.Model):
    id_tipo_medicamento = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    nombre = models.CharField(max_length=50,null=True)
    indicaciones = models.CharField(max_length=100,null=True)
    especificacion = models.CharField(max_length=100,null=True)
    enfermedad_a_tratar = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_medicamento'

class Usuario(models.Model):
    id_usuario = models.CharField(primary_key=True,max_length=10)  # This field type is a guess.
    sigla = models.CharField(max_length=50,null=True)
    correo_electronico = models.CharField(max_length=50,null=True)
    contrasena = models.CharField(max_length=50,null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


