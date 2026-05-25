from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GLDebugHelper"]

class GLDebugHelper(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/opengl/GLDebugHelper"
    __javaconstructor__ = [("()V", False)]
    CONFIG_CHECK_GL_ERROR = JavaStaticField("I")
    CONFIG_CHECK_THREAD = JavaStaticField("I")
    CONFIG_LOG_ARGUMENT_NAMES = JavaStaticField("I")
    ERROR_WRONG_THREAD = JavaStaticField("I")
    wrap = JavaMultipleMethod([("(Ljavax/microedition/khronos/opengles/GL;ILjava/io/Writer;)Ljavax/microedition/khronos/opengles/GL;", True, False), ("(Ljavax/microedition/khronos/egl/EGL;ILjava/io/Writer;)Ljavax/microedition/khronos/egl/EGL;", True, False)])