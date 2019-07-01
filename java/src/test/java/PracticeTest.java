import org.junit.jupiter.api.Test;

import java.util.*;
import java.util.function.Predicate;
import java.util.stream.Collectors;

import static java.util.Arrays.asList;
import static java.util.stream.Collectors.*;

class PracticeTest {

    @Test
    void nothing() {
        List<Practice> practices = asList(
            new Practice(20, Practice.Type.Fish, "pork"),
            new Practice(30, Practice.Type.Meat, "beef"),
            new Practice(80, Practice.Type.Fish, "chicken"),
            new Practice(10, Practice.Type.Fish, "rice"),
            new Practice(80, Practice.Type.Other, "pizza"),
            new Practice(80, Practice.Type.Fish, "salmon")
        );

        Map<String, List<String>> dishTags = new HashMap<>();
        dishTags.put("pork", asList("greasy", "salty"));
        dishTags.put("beef", asList("fat", "nice"));
        dishTags.put("rice", asList("tasty", "not-salty"));
        dishTags.put("pizza", asList("greasy", "shit-fat"));
        dishTags.put("salmon", asList("greasy", "salty"));
//        dishTags.put("chicken", asList("greasy", "salty"));


        Predicate<Practice> less_than_40_calories = (practice -> practice.getCalories() < 40);
        Map<Practice.Type, Set<Practice>> by_type = practices.stream()
                                                              .collect(Collectors.groupingBy(Practice::getType,
                                                                                             Collectors.filtering(less_than_40_calories,
                                                                                                                  toSet())));
        System.out.println(by_type);

        Map<Practice.Type, Set<String>> by_type_get_what = practices.stream()
                                                                    .filter(dish -> dishTags.containsKey(dish.getName()))
                                                                    .collect(groupingBy(Practice::getType,
                                                                                        flatMapping(dish -> dishTags.get(dish.getName())
                                                                                                                    .stream(),
                                                                                                    toSet())));
        System.out.println(by_type_get_what);
    }

    @Test
    void second_nothing() {

    }
}