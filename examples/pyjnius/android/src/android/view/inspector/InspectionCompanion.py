from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InspectionCompanion"]

class InspectionCompanion(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inspector/InspectionCompanion"
    readProperties = JavaMethod("(Ljava/lang/Object;Landroid/view/inspector/PropertyReader;)V")
    mapProperties = JavaMethod("(Landroid/view/inspector/PropertyMapper;)V")

    class UninitializedPropertyMapException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inspector/InspectionCompanion$UninitializedPropertyMapException"
        __javaconstructor__ = [("()V", False)]