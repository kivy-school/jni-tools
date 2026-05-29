from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResourceBundle"]

class ResourceBundle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/ResourceBundle"
    __javaconstructor__ = [("()V", False)]
    getObject = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    keySet = JavaMethod("()Ljava/util/Set;")
    containsKey = JavaMethod("(Ljava/lang/String;)Z")
    getLocale = JavaMethod("()Ljava/util/Locale;")
    clearCache = JavaMultipleMethod([("(Ljava/lang/ClassLoader;)V", True, False), ("()V", True, False)])
    getString = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getStringArray = JavaMethod("(Ljava/lang/String;)[Ljava/lang/String;")
    getKeys = JavaMethod("()Ljava/util/Enumeration;")
    getBundle = JavaMultipleMethod([("(Ljava/lang/String;Ljava/util/Locale;Ljava/lang/ClassLoader;Ljava/util/ResourceBundle$Control;)Ljava/util/ResourceBundle;", True, False), ("(Ljava/lang/String;Ljava/lang/Module;)Ljava/util/ResourceBundle;", True, False), ("(Ljava/lang/String;)Ljava/util/ResourceBundle;", True, False), ("(Ljava/lang/String;Ljava/util/Locale;Ljava/lang/Module;)Ljava/util/ResourceBundle;", True, False), ("(Ljava/lang/String;Ljava/util/Locale;)Ljava/util/ResourceBundle;", True, False), ("(Ljava/lang/String;Ljava/util/ResourceBundle$Control;)Ljava/util/ResourceBundle;", True, False), ("(Ljava/lang/String;Ljava/util/Locale;Ljava/util/ResourceBundle$Control;)Ljava/util/ResourceBundle;", True, False), ("(Ljava/lang/String;Ljava/util/Locale;Ljava/lang/ClassLoader;)Ljava/util/ResourceBundle;", True, False)])
    getBaseBundleName = JavaMethod("()Ljava/lang/String;")

    class Control(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/ResourceBundle$Control"
        FORMAT_DEFAULT = JavaStaticField("Ljava/util/List;")
        FORMAT_CLASS = JavaStaticField("Ljava/util/List;")
        FORMAT_PROPERTIES = JavaStaticField("Ljava/util/List;")
        TTL_DONT_CACHE = JavaStaticField("J")
        TTL_NO_EXPIRATION_CONTROL = JavaStaticField("J")
        getFormats = JavaMethod("(Ljava/lang/String;)Ljava/util/List;")
        getControl = JavaStaticMethod("(Ljava/util/List;)Ljava/util/ResourceBundle$Control;")
        getCandidateLocales = JavaMethod("(Ljava/lang/String;Ljava/util/Locale;)Ljava/util/List;")
        getFallbackLocale = JavaMethod("(Ljava/lang/String;Ljava/util/Locale;)Ljava/util/Locale;")
        newBundle = JavaMethod("(Ljava/lang/String;Ljava/util/Locale;Ljava/lang/String;Ljava/lang/ClassLoader;Z)Ljava/util/ResourceBundle;")
        needsReload = JavaMethod("(Ljava/lang/String;Ljava/util/Locale;Ljava/lang/String;Ljava/lang/ClassLoader;Ljava/util/ResourceBundle;J)Z")
        getTimeToLive = JavaMethod("(Ljava/lang/String;Ljava/util/Locale;)J")
        toBundleName = JavaMethod("(Ljava/lang/String;Ljava/util/Locale;)Ljava/lang/String;")
        toResourceName = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
        getNoFallbackControl = JavaStaticMethod("(Ljava/util/List;)Ljava/util/ResourceBundle$Control;")