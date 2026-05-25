from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PolicyUpdateResult"]

class PolicyUpdateResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/admin/PolicyUpdateResult"
    __javaconstructor__ = [("(I)V", False)]
    RESULT_FAILURE_CONFLICTING_ADMIN_POLICY = JavaStaticField("I")
    RESULT_FAILURE_HARDWARE_LIMITATION = JavaStaticField("I")
    RESULT_FAILURE_STORAGE_LIMIT_REACHED = JavaStaticField("I")
    RESULT_FAILURE_UNKNOWN = JavaStaticField("I")
    RESULT_POLICY_CLEARED = JavaStaticField("I")
    RESULT_POLICY_SET = JavaStaticField("I")
    getResultCode = JavaMethod("()I")