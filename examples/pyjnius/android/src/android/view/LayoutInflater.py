from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LayoutInflater"]

class LayoutInflater(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/LayoutInflater"
    inflate = JavaMultipleMethod([("(ILandroid/view/ViewGroup;Z)Landroid/view/View;", False, False), ("(ILandroid/view/ViewGroup;)Landroid/view/View;", False, False), ("(Lorg/xmlpull/v1/XmlPullParser;Landroid/view/ViewGroup;)Landroid/view/View;", False, False), ("(Lorg/xmlpull/v1/XmlPullParser;Landroid/view/ViewGroup;Z)Landroid/view/View;", False, False)])
    from = JavaStaticMethod("(Landroid/content/Context;)Landroid/view/LayoutInflater;")
    getFactory = JavaMethod("()Landroid/view/LayoutInflater$Factory;")
    getContext = JavaMethod("()Landroid/content/Context;")
    onCreateView = JavaMethod("(Landroid/content/Context;Landroid/view/View;Ljava/lang/String;Landroid/util/AttributeSet;)Landroid/view/View;")
    setFilter = JavaMethod("(Landroid/view/LayoutInflater$Filter;)V")
    getFactory2 = JavaMethod("()Landroid/view/LayoutInflater$Factory2;")
    setFactory2 = JavaMethod("(Landroid/view/LayoutInflater$Factory2;)V")
    cloneInContext = JavaMethod("(Landroid/content/Context;)Landroid/view/LayoutInflater;")
    createView = JavaMultipleMethod([("(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;Landroid/util/AttributeSet;)Landroid/view/View;", False, False), ("(Ljava/lang/String;Ljava/lang/String;Landroid/util/AttributeSet;)Landroid/view/View;", False, False)])
    setFactory = JavaMethod("(Landroid/view/LayoutInflater$Factory;)V")
    getFilter = JavaMethod("()Landroid/view/LayoutInflater$Filter;")

    class Filter(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/LayoutInflater$Filter"
        onLoadClass = JavaMethod("(Ljava/lang/Class;)Z")

    class Factory2(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/LayoutInflater$Factory2"
        onCreateView = JavaMethod("(Landroid/view/View;Ljava/lang/String;Landroid/content/Context;Landroid/util/AttributeSet;)Landroid/view/View;")

    class Factory(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/LayoutInflater$Factory"
        onCreateView = JavaMethod("(Ljava/lang/String;Landroid/content/Context;Landroid/util/AttributeSet;)Landroid/view/View;")