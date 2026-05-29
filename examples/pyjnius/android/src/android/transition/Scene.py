from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Scene"]

class Scene(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/Scene"
    __javaconstructor__ = [("(Landroid/view/ViewGroup;Landroid/view/View;)V", False), ("(Landroid/view/ViewGroup;)V", False), ("(Landroid/view/ViewGroup;Landroid/view/ViewGroup;)V", False)]
    getCurrentScene = JavaStaticMethod("(Landroid/view/ViewGroup;)Landroid/transition/Scene;")
    getSceneForLayout = JavaStaticMethod("(Landroid/view/ViewGroup;ILandroid/content/Context;)Landroid/transition/Scene;")
    getSceneRoot = JavaMethod("()Landroid/view/ViewGroup;")
    setEnterAction = JavaMethod("(Ljava/lang/Runnable;)V")
    setExitAction = JavaMethod("(Ljava/lang/Runnable;)V")
    exit = JavaMethod("()V")
    enter = JavaMethod("()V")