class CourseModules:
    def __init__(self):
        self.modules_list = [
            {
                "id":1,
                "module_name": "IS2",
                "teaching_language": "English"
            },
            {
                "id":2,
                "module_name": "COIN2",
                "teaching_language": "English"
            }
        ]

    def GetAllModules(self):
        if len(self.modules_list) > 0:
            return self.modules_list
        else:
            return 'No Modules Found'

    def GetModule(self,id):
        for moldule in self.modules_list:
            if moldule['id']==id:
                return moldule
            
        return 'Module Not Found'

    def AddModule(self,module_name, module_teach_medium):
        newModule = {
            "id": len(self.modules_list)+1,
            "module_name": module_name,
            "teaching_language": module_teach_medium
        }
        self.modules_list.append(newModule)
        return newModule
    
    def EditModule(self,id,module_name,module_teach_medium):
        for module in self.modules_list:
            if module['id']==id:
                module['module_name'] = module_name
                module['teaching_language'] = module_teach_medium
                return module
        return 'Not Found'
    
    def RemoveModule(self,id):
        for index,module in enumerate(self.modules_list):
            if module['id']==id:
                self.modules_list.pop(index)
                return 'Module Deleted'
        return 'Not found'

