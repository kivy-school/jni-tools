from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LayoutInflater"]

class LayoutInflater(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/LayoutInflater"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/view/LayoutInflater;Landroid/content/Context;)V", False)]
    from = JavaStaticMethod("(Landroid/content/Context;)Landroid/view/LayoutInflater;")
    cloneInContext = JavaMethod("(Landroid/content/Context;)Landroid/view/LayoutInflater;")
    getContext = JavaMethod("()Landroid/content/Context;")
    getFactory = JavaMethod("()Landroid/view/LayoutInflater$Factory;")
    getFactory2 = JavaMethod("()Landroid/view/LayoutInflater$Factory2;")
    setFactory = JavaMethod("(Landroid/view/LayoutInflater$Factory;)V")
    setFactory2 = JavaMethod("(Landroid/view/LayoutInflater$Factory2;)V")
    getFilter = JavaMethod("()Landroid/view/LayoutInflater$Filter;")
    setFilter = JavaMethod("(Landroid/view/LayoutInflater$Filter;)V")
    inflate = JavaMultipleMethod([("(ILandroid/view/ViewGroup;)Landroid/view/View;", False, False), ("(Lorg/xmlpull/v1/XmlPullParser;Landroid/view/ViewGroup;)Landroid/view/View;", False, False), ("(ILandroid/view/ViewGroup;Z)Landroid/view/View;", False, False), ("(Lorg/xmlpull/v1/XmlPullParser;Landroid/view/ViewGroup;Z)Landroid/view/View;", False, False)])
    createView = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;Landroid/util/AttributeSet;)Landroid/view/View;", False, False), ("(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;Landroid/util/AttributeSet;)Landroid/view/View;", False, False)])
    onCreateView = JavaMultipleMethod([("(Ljava/lang/String;Landroid/util/AttributeSet;)Landroid/view/View;", False, False), ("(Landroid/view/View;Ljava/lang/String;Landroid/util/AttributeSet;)Landroid/view/View;", False, False), ("(Landroid/content/Context;Landroid/view/View;Ljava/lang/String;Landroid/util/AttributeSet;)Landroid/view/View;", False, False)])

    class Factory(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/LayoutInflater/Factory"
        onCreateView = JavaMethod("(Ljava/lang/String;Landroid/content/Context;Landroid/util/AttributeSet;)Landroid/view/View;")

    class Factory2(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/LayoutInflater/Factory2"
        onCreateView = JavaMethod("(Landroid/view/View;Ljava/lang/String;Landroid/content/Context;Landroid/util/AttributeSet;)Landroid/view/View;")

    class Filter(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/LayoutInflater/Filter"
        onLoadClass = JavaMethod("(Ljava/lang/Class;)Z")