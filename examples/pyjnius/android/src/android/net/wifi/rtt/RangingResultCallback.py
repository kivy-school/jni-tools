from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RangingResultCallback"]

class RangingResultCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/rtt/RangingResultCallback"
    __javaconstructor__ = [("()V", False)]
    STATUS_CODE_FAIL = JavaStaticField("I")
    STATUS_CODE_FAIL_RTT_NOT_AVAILABLE = JavaStaticField("I")
    onRangingFailure = JavaMethod("(I)V")
    onRangingResults = JavaMethod("(Ljava/util/List;)V")