package utils;

import java.util.Collection;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

public class Counter<T> {

    private Map<T, Long> map;

    public Counter(Collection<T> collection) {
        this.map = collection.stream()
                             .collect(Collectors.groupingBy(Function.identity(),
                                                            Collectors.counting()));
    }
    public Counter(Map<T, ?> collection) {
        this.map = collection.entrySet()
                             .stream()
                             .map(Map.Entry::getKey)
                             .collect(Collectors.groupingBy(Function.identity(),
                                                            Collectors.counting()));
    }

    public Map<T, Long> getMap() {
        return map;
    }

    public void add(T elem) {
        if (map.containsKey(elem)) {
            map.replace(elem, map.get(elem) + 1);
        } else {
            map.put(elem, (long) 1);
        }
    }
}
