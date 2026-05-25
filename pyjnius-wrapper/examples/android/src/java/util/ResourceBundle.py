from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ResourceBundle"]

class ResourceBundle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/ResourceBundle"
    __javaconstructor__ = [("()V", False)]
    parent = JavaField("Ljava/util/ResourceBundle;")
    getBaseBundleName = JavaMethod("()Ljava/lang/String;")
    getString = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getStringArray = JavaMethod("(Ljava/lang/String;)[Ljava/lang/String;")
    getObject = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    getLocale = JavaMethod("()Ljava/util/Locale;")
    setParent = JavaMethod("(Ljava/util/ResourceBundle;)V")
    getBundle = JavaMultipleMethod([("(Ljava/lang/String;)Ljava/util/ResourceBundle;", True, False), ("(Ljava/lang/String;Ljava/util/ResourceBundle$Control;)Ljava/util/ResourceBundle;", True, False), ("(Ljava/lang/String;Ljava/util/Locale;)Ljava/util/ResourceBundle;", True, False), ("(Ljava/lang/String;Ljava/util/Locale;Ljava/util/ResourceBundle$Control;)Ljava/util/ResourceBundle;", True, False), ("(Ljava/lang/String;Ljava/util/Locale;Ljava/lang/ClassLoader;)Ljava/util/ResourceBundle;", True, False), ("(Ljava/lang/String;Ljava/util/Locale;Ljava/lang/ClassLoader;Ljava/util/ResourceBundle$Control;)Ljava/util/ResourceBundle;", True, False)])
    clearCache = JavaMultipleMethod([("()V", True, False), ("(Ljava/lang/ClassLoader;)V", True, False)])
    handleGetObject = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    getKeys = JavaMethod("()Ljava/util/Enumeration;")
    containsKey = JavaMethod("(Ljava/lang/String;)Z")
    keySet = JavaMethod("()Ljava/util/Set;")
    handleKeySet = JavaMethod("()Ljava/util/Set;")

    class Control(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/util/ResourceBundle/Control"
        __javaconstructor__ = [("()V", False)]
        FORMAT_CLASS = JavaStaticField("Ljava/util/List;")
        FORMAT_DEFAULT = JavaStaticField("Ljava/util/List;")
        FORMAT_PROPERTIES = JavaStaticField("Ljava/util/List;")
        TTL_DONT_CACHE = JavaStaticField("J")
        TTL_NO_EXPIRATION_CONTROL = JavaStaticField("J")
        getControl = JavaStaticMethod("(Ljava/util/List;)Ljava/util/ResourceBundle$Control;")
        getNoFallbackControl = JavaStaticMethod("(Ljava/util/List;)Ljava/util/ResourceBundle$Control;")
        getFormats = JavaMethod("(Ljava/lang/String;)Ljava/util/List;")
        getCandidateLocales = JavaMethod("(Ljava/lang/String;Ljava/util/Locale;)Ljava/util/List;")
        getFallbackLocale = JavaMethod("(Ljava/lang/String;Ljava/util/Locale;)Ljava/util/Locale;")
        newBundle = JavaMethod("(Ljava/lang/String;Ljava/util/Locale;Ljava/lang/String;Ljava/lang/ClassLoader;Z)Ljava/util/ResourceBundle;")
        getTimeToLive = JavaMethod("(Ljava/lang/String;Ljava/util/Locale;)J")
        needsReload = JavaMethod("(Ljava/lang/String;Ljava/util/Locale;Ljava/lang/String;Ljava/lang/ClassLoader;Ljava/util/ResourceBundle;J)Z")
        toBundleName = JavaMethod("(Ljava/lang/String;Ljava/util/Locale;)Ljava/lang/String;")
        toResourceName = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")