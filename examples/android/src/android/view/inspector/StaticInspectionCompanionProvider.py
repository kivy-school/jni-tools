from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StaticInspectionCompanionProvider"]

class StaticInspectionCompanionProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inspector/StaticInspectionCompanionProvider"
    __javaconstructor__ = [("()V", False)]
    provide = JavaMethod("(Ljava/lang/Class;)Landroid/view/inspector/InspectionCompanion;")