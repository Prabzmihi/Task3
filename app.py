from flask import Flask,request,jsonify
from .CourseModules import CourseModules

app = Flask(__name__);

cm = CourseModules()

@app.route('/')
def index():
    return 'This API is working.'

@app.route('/modules',methods=['GET','POST','PUT','DELETE'])
def modules():
    
    # GET Method
    if request.method == 'GET':
        modlist = cm.GetAllModules()
        if modlist == 'No Modules Found':
            return "Nothing Found", 404
        else:
            return jsonify(modlist)
    
    # POST Method
    if request.method == 'POST':

        new_module_name = request.form["module_name"]
        new_module_teaching_language = request.form["module_language"]
        
        new_module = cm.AddModule(new_module_name,new_module_teaching_language)

        return jsonify(new_module),201
    
@app.route('/module/<int:id>',methods=['GET','PUT','DELETE'])
def single_modules(id):

    #GET Single Module
    if request.method == 'GET':
        searched_module = cm.GetModule(id)
        if(searched_module == 'Module Not Found'):
            return 'Not found',404    
        else:
            return jsonify(searched_module),200
    
    #Update Single Module
    if request.method == 'PUT':

        new_module_name = request.form["module_name"]
        new_module_language = request.form["module_language"]

        modified_module = cm.EditModule(id,new_module_name,new_module_language)

        if(modified_module == 'Not Found'):
            return 'Not found',404
        else:
            return jsonify(modified_module),201  
    
    #Delete Single Module
    if request.method == 'DELETE':
        deleted = cm.RemoveModule(id)

        if(deleted == 'Not found'):
            return 'Not found',404
        else:
            return 'Module Successfully Deleted'