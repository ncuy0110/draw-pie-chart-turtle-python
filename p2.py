import turtle
def draw_pie_chart(staff_id, normal_hour_salary, night_shift_salary,
                   overtime_salary, overtime_night_shift_salary,
                   holiday_salary, supporting_fee):
    ls = turtle.Screen()
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(100,360)
    turtle.end_fill()

    total_payment = normal_hour_salary + night_shift_salary + \
                    overtime_night_shift_salary + overtime_salary + holiday_salary + supporting_fee
    # percent_n_h_s = normal_hour_salary/total_payment*360
    max = 360
    print(total_payment)
    list_type_salary = [normal_hour_salary, night_shift_salary, overtime_night_shift_salary, overtime_salary,
                        holiday_salary, supporting_fee]
    list_color = ["blue", "yellow", "green", "black", "orange"]
    list_name_salary = ["NHS","NSS","OTSS","OTS", "HS", "SF"]
    for k in range(0,5):
        turtle.begin_fill()
        turtle.color(list_color[k])
        max-=(list_type_salary[k]*360/total_payment)
        turtle.circle(100, max)
        if turtle.position()[0]<=0:
            turtle.write(list_name_salary[k]+" "+str(list_type_salary[k+1])+" ", move=False, align="right")
        else:
            turtle.write(list_name_salary[k]+" "+str(list_type_salary[k+1])+" ", move=False, align="left")
        turtle.goto(0, 100)
        turtle.goto(0, 0)
        turtle.left(360-max)
        turtle.end_fill()
    turtle.color("black")
    turtle.write(list_name_salary[5]+" "+str(list_type_salary[0])+" ", move=False, align="right")
    turtle.penup()
    turtle.goto(0, 230)
    turtle.write("Employee id "+ str(staff_id), align="center")
    ls.exitonclick()

draw_pie_chart(1, 6, 7, 8, 5, 5, 5)