from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PropertyChangeListenerProxy"]

class PropertyChangeListenerProxy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/beans/PropertyChangeListenerProxy"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/beans/PropertyChangeListener;)V", False)]
    getPropertyName = JavaMethod("()Ljava/lang/String;")
    propertyChange = JavaMethod("(Ljava/beans/PropertyChangeEvent;)V")