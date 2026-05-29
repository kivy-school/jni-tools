from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimePickerDialog"]

class TimePickerDialog(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/TimePickerDialog"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/app/TimePickerDialog$OnTimeSetListener;IIZ)V", False), ("(Landroid/content/Context;ILandroid/app/TimePickerDialog$OnTimeSetListener;IIZ)V", False)]
    onTimeChanged = JavaMethod("(Landroid/widget/TimePicker;II)V")
    show = JavaMethod("()V")
    onClick = JavaMethod("(Landroid/content/DialogInterface;I)V")
    updateTime = JavaMethod("(II)V")
    onSaveInstanceState = JavaMethod("()Landroid/os/Bundle;")
    onRestoreInstanceState = JavaMethod("(Landroid/os/Bundle;)V")

    class OnTimeSetListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/TimePickerDialog/OnTimeSetListener"
        onTimeSet = JavaMethod("(Landroid/widget/TimePicker;II)V")