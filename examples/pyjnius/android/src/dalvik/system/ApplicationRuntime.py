from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ApplicationRuntime"]

class ApplicationRuntime(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "dalvik/system/ApplicationRuntime"
    getBaseApkOptimizationInfo = JavaStaticMethod("()Ldalvik/system/DexFile$OptimizationInfo;")