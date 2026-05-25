plugins {
    java
    application
    id("com.gradleup.shadow") version "8.3.5"
}

group = "dev.kivyschool.pyjniuswrap"
version = "0.1.0"

repositories {
    mavenCentral()
}

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21)
    }
}

dependencies {
    implementation("com.github.javaparser:javaparser-symbol-solver-core:3.26.4")
    implementation("com.fasterxml.jackson.core:jackson-databind:2.18.2")
    implementation("info.picocli:picocli:4.7.6")
    implementation("org.ow2.asm:asm:9.7.1")
    testImplementation("org.junit.jupiter:junit-jupiter:5.11.4")
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")
}

application {
    mainClass = "dev.kivyschool.pyjniuswrap.JavaAstEmitter"
}

tasks.test {
    useJUnitPlatform()
    testLogging {
        events("passed", "failed", "skipped")
        showStandardStreams = true
    }
}

tasks.shadowJar {
    archiveBaseName = "java-ast-emitter"
    archiveClassifier = ""
    archiveVersion = ""
    mergeServiceFiles()
}
