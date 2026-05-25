from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MealType"]

class MealType(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/MealType"
    MEAL_TYPE_BREAKFAST = JavaStaticField("I")
    MEAL_TYPE_DINNER = JavaStaticField("I")
    MEAL_TYPE_LUNCH = JavaStaticField("I")
    MEAL_TYPE_SNACK = JavaStaticField("I")
    MEAL_TYPE_UNKNOWN = JavaStaticField("I")