from projects.models import ProjectsModel
def filters(params):
    model = ProjectsModel.objects.all()
    methods = ['text',"date_created"]
    # print(params)
    my_params = []
    print(params['alpha'])
    if params:

        if params['time'] == "new-old":
            my_params.append("date_of_creation")
        elif params['time'] == 'old-new':
            my_params.append("-date_of_creation")
        if params['alpha'] == "а-я":
            my_params.append("name_task")
        elif params['alpha'] == "я-а":
            my_params.append("-name_task")
        print(*my_params)
        model = ProjectsModel.objects.order_by(*my_params)
        return model
    else:
        return model

#сортировка по проектам по: времени создания\обновления (от старых к новым и наоборот)
#по названию от а-я
#возможность фильтрации задач
#от и до (созданные обнавленные срок и выполнение от 00.00.2000 до 00.00.2001)

#---------
#по дате создания/обновления (от старых к новым и от новых к старым)
#по названию (от а до я)