from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TriggerEventListener"]

class TriggerEventListener(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/TriggerEventListener"
    __javaconstructor__ = [("()V", False)]
    onTrigger = JavaMethod("(Landroid/hardware/TriggerEvent;)V")