from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CharacterPickerDialog"]

class CharacterPickerDialog(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/CharacterPickerDialog"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/view/View;Landroid/text/Editable;Ljava/lang/String;Z)V", False)]
    onCreate = JavaMethod("(Landroid/os/Bundle;)V")
    onItemClick = JavaMethod("(Landroid/widget/AdapterView;Landroid/view/View;IJ)V")
    onClick = JavaMethod("(Landroid/view/View;)V")