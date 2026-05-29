from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InspectionCompanionProvider"]

class InspectionCompanionProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inspector/InspectionCompanionProvider"
    provide = JavaMethod("(Ljava/lang/Class;)Landroid/view/inspector/InspectionCompanion;")