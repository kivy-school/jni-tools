from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FragmentContainer"]

class FragmentContainer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/FragmentContainer"
    __javaconstructor__ = [("()V", False)]
    onFindViewById = JavaMethod("(I)Landroid/view/View;")
    onHasView = JavaMethod("()Z")