from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InspectionCompanion"]

class InspectionCompanion(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inspector/InspectionCompanion"
    mapProperties = JavaMethod("(Landroid/view/inspector/PropertyMapper;)V")
    readProperties = JavaMethod("(Ljava/lang/Object;Landroid/view/inspector/PropertyReader;)V")

    class UninitializedPropertyMapException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inspector/InspectionCompanion/UninitializedPropertyMapException"
        __javaconstructor__ = [("()V", False)]