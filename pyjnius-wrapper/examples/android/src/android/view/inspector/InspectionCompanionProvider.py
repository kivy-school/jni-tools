from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InspectionCompanionProvider"]

class InspectionCompanionProvider(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inspector/InspectionCompanionProvider"
    provide = JavaMethod("(Ljava/lang/Class;)Landroid/view/inspector/InspectionCompanion;")