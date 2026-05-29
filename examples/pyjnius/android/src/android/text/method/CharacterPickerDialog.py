from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharacterPickerDialog"]

class CharacterPickerDialog(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/CharacterPickerDialog"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/view/View;Landroid/text/Editable;Ljava/lang/String;Z)V", False)]
    BUTTON1 = JavaStaticField("I")
    BUTTON2 = JavaStaticField("I")
    BUTTON3 = JavaStaticField("I")
    BUTTON_NEGATIVE = JavaStaticField("I")
    BUTTON_NEUTRAL = JavaStaticField("I")
    BUTTON_POSITIVE = JavaStaticField("I")
    onClick = JavaMethod("(Landroid/view/View;)V")
    onItemClick = JavaMethod("(Landroid/widget/AdapterView;Landroid/view/View;IJ)V")