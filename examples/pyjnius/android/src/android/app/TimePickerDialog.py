from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimePickerDialog"]

class TimePickerDialog(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/TimePickerDialog"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/app/TimePickerDialog$OnTimeSetListener;IIZ)V", False), ("(Landroid/content/Context;ILandroid/app/TimePickerDialog$OnTimeSetListener;IIZ)V", False)]
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
    updateTime = JavaMethod("(II)V")
    onClick = JavaMethod("(Landroid/content/DialogInterface;I)V")
    onRestoreInstanceState = JavaMethod("(Landroid/os/Bundle;)V")
    onSaveInstanceState = JavaMethod("()Landroid/os/Bundle;")
    show = JavaMethod("()V")
    onTimeChanged = JavaMethod("(Landroid/widget/TimePicker;II)V")

    class OnTimeSetListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/TimePickerDialog$OnTimeSetListener"
        onTimeSet = JavaMethod("(Landroid/widget/TimePicker;II)V")