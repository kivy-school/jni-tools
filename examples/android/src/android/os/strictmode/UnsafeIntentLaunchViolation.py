from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnsafeIntentLaunchViolation"]

class UnsafeIntentLaunchViolation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/strictmode/UnsafeIntentLaunchViolation"
    __javaconstructor__ = [("(Landroid/content/Intent;)V", False)]
    getIntent = JavaMethod("()Landroid/content/Intent;")