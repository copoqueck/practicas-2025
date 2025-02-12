-- ¿Cuáles son los empleados y su año de ingreso que tienen más de dos hijos y
-- trabajan en departamentos con menos de 4000€ de presupuesto

/*
 * Base de datos:  bd_empleados
 *
 * Tabla: t_empleados
 *
 *  nombre_empleado |   fecha_ingreso_empleado  |   num_hijos |   id_departamento
 *  ----------------|---------------------------|-------------|-------------------
 *  GIL, GLORIA     |   1950                    |   1         |   1
 *  PONS, CESAR     |   1997                    |   2         |   2
 *  VEIGA, JULIANA  |   1980                    |   2         |   3
 *  FLOR, DOROTEA   |   1959                    |   3         |   4
 *
 * Tabla: t_departamentos
 * id_departamento |   presupuesto
 * ----------------|---------------
 *       1         |   3000
 *       2         |   5000
 *       3         |   2000
 *       4         |   6000
 */

 select nombre_empleado, fecha_ingreso_empleado from t_empleados
where num_hijos > 2 and id_departamento in (
    select id_departamento from t_departamentos where presupuesto < 4000
);


