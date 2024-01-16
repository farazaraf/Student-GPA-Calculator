from nicegui import ui
import joblib

centralized = ui.row().style("margin:auto;")

with centralized:
    ui.markdown('###Welcome to Student GPA Prediction App!')
with ui.row().style("margin:auto;"):
    ui.markdown('Please enter SGPA in your first four semesters in **X.XX** format:')

sem1 = 0.0
sem2 = 0.0
sem3 = 0.0
sem4 = 0.0
prediction_model = 'gpa_prediction_model_gradientbooster.joblib'

def on_change_callback1(e):
    global sem1  # Assuming sem1 is a variable defined outside this function
    sem1 = e.value
def on_change_callback2(e):
    global sem2  # Assuming sem1 is a variable defined outside this function
    sem2 = e.value
def on_change_callback3(e):
    global sem3  # Assuming sem1 is a variable defined outside this function
    sem3 = e.value
def on_change_callback4(e):
    global sem4  # Assuming sem1 is a variable defined outside this function
    sem4 = e.value

def choose_model(e):
    global prediction_model
    if e.value == 1:
        prediction_model = 'gpa_prediction_model_gradientbooster.joblib'
    elif e.value == 2:
        prediction_model = 'gpa_prediction_model_randomforest.joblib'
    elif e.value == 3:
        prediction_model = 'gpa_prediction_model_decisiontree.joblib'

def calculate_cgpa(gpa_list):
    # Calculate CGPA
    cgpa = sum(gpa_list) / 5.0
    return cgpa
   
def Prediction():
    model = joblib.load(prediction_model)
    new_features = [sem1,sem2,sem3,sem4]
    predictions = model.predict([new_features])
    new_features.append(predictions[0])
    sgpa_result = f"Your SGPA for fifth semester will be:{predictions[0]:.2f}"
    cgpa_result = f"Your CGPA will be: {calculate_cgpa(new_features):.2f}"
    sgpa.set_text(sgpa_result)
    cgpa.set_text(cgpa_result)
    #debug
    print(new_features)
    print(predictions)

    if 3.51 <= predictions[0] <= 4.00:
        remarks.set_text("Extraordinary Performance")
        remarks.style("color:green;")
    elif 3.00 <= predictions[0] <= 3.50:
        remarks.set_text("Very Good Performance")
        remarks.style("color:lime;")
    elif 2.51 <= predictions[0] <= 2.99:
        remarks.set_text("Good Performance")
        remarks.style("color:orange;")
    elif 2.00 <= predictions[0] <= 2.50:
        remarks.set_text("Satisfactory Performance")
        remarks.style("color:olive;")
    elif 1.00 <= predictions[0] <= 1.99:
        remarks.set_text("Poor Performance")
        remarks.style("color:maroon;")
    elif 0.00 <= predictions[0] <= 0.99:
        remarks.set_text("Very Poor Performance")
        remarks.style("color:red;")
    else:
        print("Invalid GPA value")

first_row = ui.row().style('margin:auto;')

with first_row:
    with ui.column():
        ui.markdown(f'**GPA in Semester1:**')
        ui.number(value=0, format='%.2f',max=4.0,min=0.0,step=0.1,on_change=on_change_callback1) 
    with ui.column():
        ui.markdown(f'**GPA in Semester2:**')
        ui.number(value=0, format='%.2f',max=4.0,min=0.0,step=0.1,on_change=on_change_callback2)
    with ui.column():
        ui.markdown(f'**GPA in Semester3:**')
        ui.number(value=0, format='%.2f',max=4.0,min=0.0,step=0.1,on_change=on_change_callback3)
    with ui.column():
        ui.markdown(f'**GPA in Semester4:**')
        ui.number(value=0, format='%.2f',max=4.0,min=0.0,step=0.1,on_change=on_change_callback4)

# result = ui.label()
ui.label('Choose prediction model:').style("margin:auto;font-weight: bold;")
select1 = ui.select({1:'Gradient Booster', 2:'Random forest', 3:'Decision Tree'}, value=1,on_change=choose_model).style("margin:auto;")
ui.button('Click me!', on_click=Prediction).style("margin:auto;")
sgpa = ui.label("")
cgpa = ui.label("")
remarks = ui.label()
ui.run(title="Student GPA Calculator",native=True,window_size=(800,600),reload=False)