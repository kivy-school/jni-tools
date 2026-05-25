from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DatePickerDialog"]

class DatePickerDialog(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/DatePickerDialog"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/content/Context;I)V", False), ("(Landroid/content/Context;Landroid/app/DatePickerDialog$OnDateSetListener;III)V", False), ("(Landroid/content/Context;ILandroid/app/DatePickerDialog$OnDateSetListener;III)V", False)]
    onDateChanged = JavaMethod("(Landroid/widget/DatePicker;III)V")
    setOnDateSetListener = JavaMethod("(Landroid/app/DatePickerDialog$OnDateSetListener;)V")
    onClick = JavaMethod("(Landroid/content/DialogInterface;I)V")
    getDatePicker = JavaMethod("()Landroid/widget/DatePicker;")
    updateDate = JavaMethod("(III)V")
    onSaveInstanceState = JavaMethod("()Landroid/os/Bundle;")
    onRestoreInstanceState = JavaMethod("(Landroid/os/Bundle;)V")

    class OnDateSetListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/DatePickerDialog/OnDateSetListener"
        onDateSet = JavaMethod("(Landroid/widget/DatePicker;III)V")