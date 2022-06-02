my_global_var = "Hola global"


def ejemplificar_scope_vars(param):
    global my_global_var
    if param != "":
        param_lower = param.lower()
        print(param_lower)
        if len(param_lower) > 2:
            param_upper = param.upper()
            my_global_var = my_global_var.upper()
            print(param_upper)


def ejemplificar_scope_vars_2():
    global my_global_var
    print(my_global_var)


ejemplificar_scope_vars("Holis")
ejemplificar_scope_vars_2()

print("==================================")


counter = 0


def contar_apariciones(param):
    global counter
    if param.startswith("8"):
        print(param, "counter before increase", counter)
        counter += 1
        print("Counter after increase", counter)
    else:
        print("==========================")
        print("No empieza con 8", param)
        print("==========================")


def determinar_counter_par():
    global counter
    print(counter % 2 == 0)


contar_apariciones("8465")  # => 1
determinar_counter_par()
contar_apariciones("456")  # => 1
determinar_counter_par()
contar_apariciones("988")  # => 1
determinar_counter_par()
contar_apariciones("887687")  # => 2
determinar_counter_par()
contar_apariciones("5468")  # => 2
determinar_counter_par()
contar_apariciones("8468")  # => 3
determinar_counter_par()
print(counter)  # => 2
