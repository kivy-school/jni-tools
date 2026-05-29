from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DatePickerDialog"]

class DatePickerDialog(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/DatePickerDialog"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;ILandroid/app/DatePickerDialog$OnDateSetListener;III)V", False), ("(Landroid/content/Context;I)V", False), ("(Landroid/content/Context;Landroid/app/DatePickerDialog$OnDateSetListener;III)V", False)]
    THEME_DEVICE_DEFAULT_DARK = JavaStaticField("I")
    THEME_DEVICE_DEFAULT_LIGHT = JavaStaticField("I")
    THEME_HOLO_DARK = JavaStaticField("I")
    THEME_HOLO_LIGHT = JavaStaticField("I")
    THEME_TRADITIONAL = JavaStaticField("I")
    BUTTON1 = JavaStaticField("I")
    BUTTON2 = JavaStaticField("I")
    BUTTON3 = JavaStaticField("I")
    BUTTON_NEGATIVE = JavaStaticField("I")
    BUTTON_NEUTRAL = JavaStaticField("I")
    BUTTON_POSITIVE = JavaStaticField("I")
    getDatePicker = JavaMethod("()Landroid/widget/DatePicker;")
    setOnDateSetListener = JavaMethod("(Landroid/app/DatePickerDialog$OnDateSetListener;)V")
    onClick = JavaMethod("(Landroid/content/DialogInterface;I)V")
    onRestoreInstanceState = JavaMethod("(Landroid/os/Bundle;)V")
    onSaveInstanceState = JavaMethod("()Landroid/os/Bundle;")
    updateDate = JavaMethod("(III)V")
    onDateChanged = JavaMethod("(Landroid/widget/DatePicker;III)V")

    class OnDateSetListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/DatePickerDialog$OnDateSetListener"
        onDateSet = JavaMethod("(Landroid/widget/DatePicker;III)V")